import logo_large from "./assets/panacea-large.png"
import logo_small from "./assets/panacea-small.png"

function Navbar() {

  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return( 
    <div className="w-full h-full absolute
    bg-gradient-to-r from-green-500 to-emerald-700">
      <header className='flex justify-between
      items-center text-black py-6 px-8
      md:px-32 bg-white drop-shadow-md'>
        <a href="#">
          <img src={logo_large} alt="" className='h-14 w-32
          hover:scale-105 transition-all hidden lg:block'/>

          <img src={logo_small} alt="" className='h-14 w-16
          hover:scale-105 transition-all lg:hidden md:block'/>
        </a>

        <ul className="hidden xl:flex items-center
        gap-12 font-semibold text-base">
          <li className="p-3 hover:bg-emerald-900
          hover:text-white rounded-md
          transition-all cursor-pointer">Home</li>
          <li className="p-3 hover:bg-emerald-900
          hover:text-white rounded-md
          transition-all cursor-pointer">Products</li>
          <li className="p-3 hover:bg-emerald-900
          hover:text-white rounded-md
          transition-all cursor-pointer">Explore</li>
          <li className="p-3 hover:bg-emerald-900
          hover:text-white rounded-md
          transition-all cursor-pointer">Contact</li>
        </ul>

        <div className='relative hidden md:flex
        items-center justify-center gap-3'>
          <i className='bx bx-search absolute left-3
          text-2xl text-gray-500 flex items-center'></i>
          <input type="text" placeholder='Search...'
          className='py-2 pl-10 rounded-xl border-2
          border-emerald-600 focus:bg-slate-100
          focus:outline-emerald-500'/>
        </div>

        <i className='bx bx-menu xl:hidden block
        text-5xl cursor-pointer' onClick={() => setIsMenuOpen(!isMenuOpen)}>
        </i>

        <div className={`absolute xl:hidden top-24
          left-0 w-full bg-white flex flex-column
          items-center gap-6 font-semibold text-lg
          transform transition-transform
          ${isMenuOpen ? "opacity-100" : "opacity-0"}`}
          style={{transition: "transform 0.3s easy, opacity 0.3s easy"}}
        >
            <li className='list-none w-full text-center
            p-4 hover:bg-emerald-900 hover:text-white
            transition-all cursor-pointer'>Home</li>

            <li className='list-none w-full text-center
            p-4 hover:bg-emerald-900 hover:text-white
            transition-all cursor-pointer'>Products</li>

            <li className='list-none w-full text-center
            p-4 hover:bg-emerald-900 hover:text-white
            transition-all cursor-pointer'>Explore</li>

            <li className='list-none w-full text-center
            p-4 hover:bg-emerald-900 hover:text-white
            transition-all cursor-pointer'>Contact</li>
        </div>
      </header>
    </div>
  )
  
}

export default Navbar
