import React from 'react';
import axios from 'axios';
import { Button } from 'antd';
import '../header/header.css'
import {useNavigate} from 'react-router-dom'
import { useEffect } from "react";
import { useState } from "react";




function Header() {

    const [status,setStatus] = useState('Войти');

    const navigate = useNavigate();

    const redirect_auth= () => {
        navigate('/auth')
    }
    useEffect(() => {
        checkStatus()
      }, []);


    const clickStatus = () =>{
        if (status == 'Выйти'){
            axios.post(
                'http://127.0.0.1:8000/auth/jwt/logout',
                { withCredentials: true }
                ).then( r=> {
                    console.log(r)
                    setStatus('Войти')
                }
                    
                ).catch((error) => {
                    if(error.status == 401){
                        console.log(error)
                        alert('Действие не было завершено')
                    }
                  }
                )
        } else{
            redirect_auth()
        } 
    }

    const checkStatus = () =>{
        axios.get(
            'http://127.0.0.1:8000/users/check',
            { withCredentials: true }
            ).then( r => {
                console.log(r)
                setStatus('Сменить аккаунт')
            }
            ).catch((error) => {
                if(error.status == 401){
                    setStatus('Войти')
                }
              }
            )
    }

    return(
        <>
            <header className='header_block'>
                <div className="header_div">
                    <a href="" className='header_title'>
                        <div className='header_title-item'>
                            NSCheck
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
                        <Button type="primary" className='header_auth' onClick={clickStatus}>
                            {status}
                        </Button>
                    </div>
                </div>
            </header> 
        </>
    )
}



export default Header;