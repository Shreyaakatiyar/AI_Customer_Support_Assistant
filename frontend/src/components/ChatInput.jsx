import { useState } from "react";

function ChatInput({ sendMessage, loading }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (!question.trim()) return;

    sendMessage(question);
    setQuestion("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSubmit();
    }
  };

  return (
    <div className="chat-input">
      <input
        type="text"
        placeholder="Ask a customer support question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={loading}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Sending..." : "Send"}
      </button>
    </div>
  );
}

export default ChatInput;