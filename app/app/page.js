"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const userLiquor = "whiskey";
    const userFlavor = "sweet";
    const userMood = "celebratory";
    const queryString = new URLSearchParams({
      liquor: userLiquor,
      flavor: userFlavor,
      mood: userMood,
    });
    const url = `http://127.0.0.1:8000/cocktail?${queryString}`;
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
        </ul>
      </div>
    </main>
  );
}
