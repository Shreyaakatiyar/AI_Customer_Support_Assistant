import ChatMessage from "./ChatMessage";

function ChatWindow({ messages, loading }) {
  return (
    <div className="chat-window">
      {messages.map((message, index) => (
        <ChatMessage
          key={index}
          message={message}
        />
      ))}

      {loading && (
        <div className="message ai-message">
          Thinking...
        </div>
      )}
    </div>
  );
}

export default ChatWindow;