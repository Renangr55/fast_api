import  Logo  from '../images/globoEsporte.png';
import styles from '../styles/Header.module.css'

const Header = () => {
    return (

        <div className={styles.config}>
            <img src={Logo} alt="logo" />

            <nav>
                <ul>
                    <li><a href="">Teams</a></li>
                    <li><a href="">About</a></li>
                    <li><a href="">Brand</a></li>
                </ul>
            </nav>
        </div>

            
      
    )
}

export default Header

