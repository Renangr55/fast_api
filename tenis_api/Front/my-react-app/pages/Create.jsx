import React from "react"
import { Header } from "../components/Header"
import { Navbar } from "../components/Navbar";
import { Footer } from "../components/Footer";
import { useState } from "react";
import { Link } from "react-router";


const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Dados enviados:', formData);
    // Aqui você pode fazer um fetch ou axios para enviar para o back-end
};

export const Create = () => {
    return (
        <div className="grid grid-rows-[auto_1fr_auto] min-h-screen">
            <Header />
        
            <div className="grid grid-cols-[250px_1fr]">
               
                <Navbar />
            
                <main className="bg-white p-6 flex justify-center items-center">
                    
                    
                    <form onSubmit={handleSubmit} className=" w-200 h-170 bg-gray-900 max-w-md mx-auto p-4 border rounded block font-bold">
                        <h1 className="text-white flex justify-self-center items-center">Create</h1>
                        <div className="mb-4">
                            <label  htmlFor="name" className=" text-amber-50 block font-bold">name:</label>
                            <input
                            type="text"
                            id="name"
                            name="name"
                          
                            className="bg-white w-full border p-2 rounded text-black"
                            />
                        </div>

                         <div className="mb-4">
                            <label  htmlFor="brand" className=" text-amber-50 block font-bold">brand:</label>
                            <input
                            type="text"
                            id="brand"
                            name="brand"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="price" className=" text-amber-50 block font-bold">price:</label>
                            <input
                            type="text"
                            id="price"
                            name="price"
                          
                            className="bg-white w-full border p-2 rounded   text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="gender" className=" text-amber-50 block font-bold">gender:</label>
                            <input
                            type="text"
                            id="gender"
                            name="gender"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="numbering" className=" text-amber-50 block font-bold">numbering:</label>
                            <input
                            type="text"
                            id="nome"
                            name="nome"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="Color" className=" text-amber-50 block font-bold">Color:</label>
                            <input
                            type="text"
                            id="color"
                            name="color"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="description" className=" text-amber-50 block font-bold">description:</label>
                            <input
                            type="text"
                            id="description"
                            name="description"
                        
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>




                        <button type="submit" className="bg-blue-500 text-white p-2 rounded w-103">
                            <Link to="/home">Submit</Link>
                        </button>
                        
                    </form>

                </main>
        
            </div>
        
            <Footer />
        </div>
    )
}