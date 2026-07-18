import { useState } from "react";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import API from "./services/api";

function App() {
  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "Hello! I'm your AI Customer Support Assistant. How can I help you today?",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async (question) => {
    if (!question.trim()) return;

    const userMessage = {
      sender: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await API.post("/chat", {
        question,
      });

      const aiMessage = {
        sender: "ai",
        text: response.data.answer,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Something went wrong. Please try again.",
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <Header />

      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ChatInput
        sendMessage={sendMessage}
        loading={loading}
      />
    </div>
  );
}

export default App;