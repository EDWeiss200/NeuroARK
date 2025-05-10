import React from 'react';
import { Divider, List, Typography } from 'antd';
import '../news/news.css';
import axios from 'axios';
import { useEffect } from "react";
import { useState } from "react";



function News  () {

    const [data,setData] = useState([]);

    useEffect(() => {
        getNews()
    }, []);

    const getNews = () => {
        axios.get(
            'http://213.171.15.163/api/news/get_news/',
            { withCredentials: true }
            ).then( r => {

                setData(r.data.map(news => ({
                    title: news[0],
                    url: news[1],
                    info: news[2]
                })));
            }
            ).catch((error) => {
                console.log(error)
            }
            )
    }

  return ( // Изменил <> на return()
    
    <div className='news'>
    <h2 className='news_title'>НОВОСТИ</h2>
    <List

    itemLayout="horizontal"
    dataSource={data}
    renderItem={(item, index) => (
      <List.Item className = 'news_list'>
        <List.Item.Meta
          title={<a href={item.url}>{item.title}</a>}
          description={item.info}

        />
      </List.Item>
    )}
     />
    </div>
    
  ); // Добавил закрывающую скобку для return
};
export default News;