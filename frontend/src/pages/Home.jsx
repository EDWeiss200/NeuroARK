import React from 'react';
import { Button, Checkbox, Form, Input } from 'antd';
import { useState } from 'react';
import axios from 'axios';
import '../index.css'
import { redirect } from "react-router-dom"
import { useNavigate } from 'react-router-dom';
import Header from '../components/header/header'
import Body from '../components/body/body';
import News from '../components/news/news';



const Home = () => {

    return(
        <>
          <Header/>
          <Body/>
          <News/>
        </>
    )
}



export default Home;