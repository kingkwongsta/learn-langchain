"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const userLiquor = "vodka";
    const userFlavor = "sour";
    const userMood = "celebratory";
    const queryString = new URLSearchParams({
      liquor: userLiquor,
      flavor: userFlavor,
      mood: userMood,
    });
    const baseUrl =
      process.env.NODE_ENV === "production"
        ? `https://langchain-backend-alpha.vercel.app/cocktail?${queryString}`
        : `/cocktail?${queryString}`;

    const url = `${baseUrl}?${queryString}`;
    // const url = `/cocktail?${queryString}`;
    // const url = `http://127.0.0.1:8000/cocktail?${queryString}`;
    const res = await fetch(url);
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
      <div>
        <ul>
          <li>{data && data.name}</li>
          <li>{data && data.description}</li>
        </ul>
      </div>
    </main>
  );
}
