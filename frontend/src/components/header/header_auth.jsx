import React from 'react';
import axios from 'axios';
import { Button } from 'antd';
import '../header/header_auth.css'
import {useNavigate} from 'react-router-dom'
import { useEffect } from "react";




function HeaderAuth() {

    const navigate = useNavigate();

    const redirect_auth= () => {
        navigate('/auth')
    }

    return(
        <>
            <header className='header_block'>
                <div className="header_div">
                    <a href="/" className='header_title'>
                        <div className='header_title-item'>
                            NSCheck
                        </div>
                    </a>
                </div>
            </header> 
        </>
    )
}



export default HeaderAuth;