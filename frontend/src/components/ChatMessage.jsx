function ChatMessage({ message }) {
  return (
    <div
      className={`message ${
        message.sender === "user"
          ? "user-message"
          : "ai-message"
      }`}
    >
      {message.text}
    </div>
  );
}

export default ChatMessage;