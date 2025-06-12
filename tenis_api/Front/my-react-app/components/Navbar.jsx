export const Navbar = () => {
    return(
        <aside className="bg-gray-900 text-white p-4 min-h-full">
          <nav className="flex justify-center items-center">
            <ul className="space-y-2">
              <li><a href="#" className="hover:text-gray-300">Create</a></li>
              <li><a href="#" className="hover:text-gray-300">Delete</a></li>
              <li><a href="#" className="hover:text-gray-300">Update</a></li>
              <li><a href="#" className="hover:text-gray-300">Read</a></li>
            </ul>
          </nav>
        </aside>
    )
}