import React from "react"
import { Header } from "../components/Header"
import banner from "../src/assets/banner.png"


export const Home = () => {
  return (
    <div className="grid grid-rows-[auto_1fr_auto] min-h-screen">
      {/* Header no topo */}
      <Header />

      {/* Grid com Sidebar e Main */}
      <div className="grid grid-cols-[250px_1fr]">
        {/* Sidebar */}
        <aside className="bg-gray-800 text-white p-4 min-h-full">
          <nav>
            <ul className="space-y-2">
              <li><a href="#" className="hover:text-gray-300">Dashboard</a></li>
              <li><a href="#" className="hover:text-gray-300">Produtos</a></li>
              <li><a href="#" className="hover:text-gray-300">Configurações</a></li>
            </ul>
          </nav>
        </aside>

        {/* Main */}
        <main className="bg-white p-6 flex justify-center items-center">
          <img className="w-250" src={banner} alt="" />
        </main>
      </div>

      {/* Footer fixo abaixo da página */}
      <footer className="bg-gray-200 text-center py-4">
        © 2025 - Seu Projeto
      </footer>
    </div>
  );
};
