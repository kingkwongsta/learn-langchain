"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const res = await fetch("http://127.0.0.1:8000/cocktail");
    const data = await res.json();
    setData(data);
  };

  return (
    <main>
      <div>HELLO WORLD</div>
      <button
        onClick={() => fetchData()}
        className="border-2 border-cyan-500 p-3"
      >
        Get Data
      </button>
      <button
        onClick={() => console.log(data)}
        className="border-2 border-cyan-500 p-3"
      >
        Print Data
      </button>
    </main>
  );
}
