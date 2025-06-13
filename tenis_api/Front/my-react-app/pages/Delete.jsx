import React from "react"
import { Header } from "../components/Header"
import { Navbar } from "../components/Navbar";
import { Footer } from "../components/Footer";
import { Link } from "react-router";



const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Dados enviados:', formData);
    // Aqui você pode fazer um fetch ou axios para enviar para o back-end
};



export const Delete = () => {
    


    return (
        <div className="grid grid-rows-[auto_1fr_auto] min-h-screen">
            <Header />
        
            <div className="grid grid-cols-[250px_1fr]">
                
                <Navbar />
            
                <main className="bg-white p-6 flex justify-center items-center">
                    
                    
                    <form onSubmit={handleSubmit} className=" w-200 h-60 bg-gray-900 max-w-md mx-auto p-4 border rounded block font-bold">
                        <h1 className="text-white flex justify-self-center items-center">Delete</h1>
                        
                        <div className="mb-4">

                            <label  htmlFor="ID" className=" text-amber-50 block font-bold">ID</label>
                            <input
                            type="number"
                            id="ID"
                            name="ID"
                            
                            className="bg-white w-full border p-2 rounded text-black"
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