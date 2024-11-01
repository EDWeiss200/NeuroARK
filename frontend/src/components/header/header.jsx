import React from 'react';
import axios from 'axios';
import { Button } from 'antd';
import '../header/header.css'





function Header() {

    return(
        <>
            <header className='header_block'>
                <div className="header_div">
                    <a href="" className='header_title'>
                        <div className='header_title-item'>
                            NCCheck
                        </div>
                    </a>
                    <div className="header_nav">
                        <ul className="header_list">
                            <li className="header_list-item">
                                <a href="" className="header_list-item_link">
                                    Проверка
                                </a>
                            </li>
                            <li className="header_list-item">
                                <a href="" className="header_list-item_link">
                                    О нас
                                </a>
                            </li>
                            <li className="header_list-item">
                                <a href="" className="header_list-item_link">
                                    Новости
                                </a>
                            </li>
                            <li className="header_list-item">
                                <a href="" className="header_list-item_link">
                                    Статистика
                                </a>
                            </li>
                        </ul>
                        <Button type="primary" className='header_auth'>
                            Войти/Выйти
                        </Button>
                    </div>
                </div>
            </header> 
        </>
    )
}



export default Header;