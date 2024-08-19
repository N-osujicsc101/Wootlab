import React, { useState } from 'react';
import { GoogleGenerativeAI } from '@google/generative-ai'; 

export default function PoemBox() {
  const [name, setName] = useState('');
  const [question, setquestion] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState(null);

  const fetchQuote = async () => {
    try {
      const genAI = new GoogleGenerativeAI('apikey'); 
      const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

      
      const prompt = `Analyze the question ${question} asked by ${name} and generate the best answer for it. start the question by saying " Hi ${name}, im glad you asked!! "  

`;

      const result = await model.generateContent(prompt);
      const text = result.response.text();
      setResponse(text);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetchQuote(); 
  };

  return (
    <div>
        <header>
        <h1>THE <span>MINI</span> ITK</h1>
      </header>
      <h2>Ask me anything, Im a <span>"know it all"</span>😃 (∩｀-´)⊃━☆ﾟ.*･｡ﾟ</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <label htmlFor="question">Question:</label>
        <input
          type="text"
          id="question"
          value={question}
          onChange={(e) => setquestion(e.target.value)}
          required
        />

        <button type="submit">Generate Answers</button>
      </form>

      {error ? <p style={{ color: 'red' }}>{error}</p> : <p>{response}</p>}
      <footer>
    <p>&copy; 2023 The Mini ITK </p>
    <p>disclaimer: Please this mini ITK doesnt really know all , abegg...dont take anything it says for truth Thank you for using mini ITK and have an awesome day💋</p>
  </footer>
      
    </div>
  );
}
