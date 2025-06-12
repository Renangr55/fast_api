
import React from 'react';
import { Link } from 'react-router';

export const Navbar = () => {
    return(
        <aside className="bg-gray-900 text-white p-4 min-h-full">
          <nav className="flex justify-center items-center">
            <ul className="space-y-2">
              <li><a href="/create" className="hover:text-gray-300">Create</a></li>
              
              <li>
                <a href="/delete" className="hover:text-gray-300">Delete</a>
              </li>
              
              <li>
                <Link to="/update" className="hover:text-gray-300">Update</Link>
              </li>
              
              <li>
                <Link to="" className="hover:text-gray-300">Read </Link>
              </li>


            </ul>
          </nav>
        </aside>
    )
}