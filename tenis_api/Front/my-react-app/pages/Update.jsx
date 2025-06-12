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

export const Update = () => {
    return (
        <div className="grid grid-rows-[auto_1fr_auto] min-h-screen">
            <Header />
        
            <div className="grid grid-cols-[250px_1fr]">
               
                <Navbar />
            
                <main className="bg-white p-6 flex justify-center items-center">
                    
                    
                    <form onSubmit={handleSubmit} className=" w-200 h-200 bg-gray-900 max-w-md mx-auto p-4 border rounded block font-bold">
                        <h1 className="text-white flex justify-self-center items-center">Update</h1>
                        
                        <div className="mb-4">
                            <label  htmlFor="id" className=" text-amber-50 block font-bold">ID:</label>
                            <input
                            type="id"
                            id="id"
                            name="id"
                            
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="name" className=" text-amber-50 block font-bold">name:</label>
                            <input
                            type="name"
                            id="name"
                            name="name"
                          
                            className="bg-white w-full border p-2 rounded text-black"
                            />
                        </div>
                        
                        <div className="mb-4">
                            <label  htmlFor="brand" className=" text-amber-50 block font-bold">brand:</label>
                            <input
                            type="brand"
                            id="brand"
                            name="brand"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="price" className=" text-amber-50 block font-bold">price:</label>
                            <input
                            type="price"
                            id="price"
                            name="price"
                          
                            className="bg-white w-full border p-2 rounded   text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="gender" className=" text-amber-50 block font-bold">gender:</label>
                            <input
                            type="gender"
                            id="gender"
                            name="gender"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="numbering" className=" text-amber-50 block font-bold">numbering:</label>
                            <input
                            type="numbering"
                            id="numbering"
                            name="numbering"
                          
                            className="bg-white w-full border p-2 rounded  text-black"
                            />
                        </div>

                        <div className="mb-4">
                            <label  htmlFor="color" className=" text-amber-50 block font-bold">color:</label>
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
                            type="description"
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