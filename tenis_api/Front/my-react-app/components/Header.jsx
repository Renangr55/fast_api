import React from "react"
import airJordan from "../src/assets/air-jordan.png";
import { TfiAlignJustify } from "react-icons/tfi";



export const Header = () => {
    return (
        <div className="bg-black w-100% h-100{%} flex justify-between">
            <img className="w-20 h-20" src={airJordan} alt="" />
            
            <nav className="flex justify-center items-center">
                <ul className="flex justify-center items-center gap-3	">
                    <li><a href="" className="text-white">Shoes</a></li>
                    <li><a href="" className="text-white">Brand</a></li>
                    <li><a href="" className="text-white">JordamX</a></li>
                </ul>
            </nav>

            <div className="flex justify-center items-center p-4">
                < TfiAlignJustify color="white"/>
            </div>



            

            
        </div>
    )
}