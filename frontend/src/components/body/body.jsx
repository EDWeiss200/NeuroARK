import React from 'react';
import axios from 'axios';
import { Button } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import '../body/body.css'
import {  message, Upload } from 'antd';
const { Dragger } = Upload;

const props = {
    name: 'file',
    multiple: true,
    // запрос
    action: 'https://660d2bd96ddfa2943b33731c.mockapi.io/api/upload',
    onChange(info) {
      const { status } = info.file;
      if (status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (status === 'done') {
        message.success(`${info.file.name} file uploaded successfully.`);
        // проверка
      } else if (status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };


function Body() {

    return(
        <>
            <section className='first'>
                <div className="first_div">
                    <div className="info_div">
                        <div className="h_div">
                            Проверка онкологии нейросетью
                        </div>
                        <div className="p_div">
                            отправте нам фотографию с потенциальным новообразованием и наша нейронная сеть проверит это
                        </div>
                    </div>  
                    <div className="send_image_div">
                        <div className="input">
                            <Dragger {...props}>
                                <p className="ant-upload-drag-icon">
                                <InboxOutlined />
                                </p>
                                <p className="ant-upload-text">Нажмите или перетащите файл в эту область для загрузки</p>
                            </Dragger>
                        </div>
                    </div>
                </div>
                <div className="first_background"></div>
            </section>
        </>
    )
}



export default Body;