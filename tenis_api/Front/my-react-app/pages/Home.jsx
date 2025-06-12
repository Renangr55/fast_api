import React from "react"
import { Header } from "../components/Header"
import banner from "../src/assets/banner.png"
import { Navbar } from "../components/Navbar";
import { Footer } from "../components/Footer";

export const Home = () => {
  return (
    <div className="grid grid-rows-[auto_1fr_auto] min-h-screen">
      <Header />

      <div className="grid grid-cols-[250px_1fr]">
       
        <Navbar />

        <main className="bg-white p-6 flex justify-center items-center">
          <img className="size-150-150" src={banner} alt="" />
        </main>

      </div>

      <Footer />
    </div>
  );
};
