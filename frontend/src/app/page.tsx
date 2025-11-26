'use client'

import { useEffect } from "react";


async function getAllExercises() {
  const url = "http://localhost:8000/exercise"

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`)
    }

    const result = await response.json();
    console.log(result);
  } catch (error: unknown) {

    if (error instanceof Error) {
      console.error(error.message);
    } else {
      console.error("Unknown error has occurred!")
    }
  }
}

export default function Home() {
  useEffect(() => {
    getAllExercises();
  }, []);

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-900 font-sans text-white dark:bg-black">
      HI
    </div>
  );
}
