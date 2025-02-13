import React from 'react';
import axios from 'axios';
import { Button } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import '../body/body.css'
import {  message, Upload, Modal } from 'antd';

const { Dragger } = Upload;
const [modalVisible, setModalVisible] = useState(false);
const [modalContent, setModalContent] = useState('');

const showModal = (content) => {
  setModalContent(content);
  setModalVisible(true);
};

const hideModal = () => {
  setModalVisible(false);
  setModalContent('');
};
const props = {
  name: 'file',
  multiple: true,
  action: 'http://213.171.15.163/api/cancers/send_photo',
  onChange(info) {
    const { status } = info.file;

    if (status !== 'uploading') {
      console.log(info.file, info.fileList);
    }

    if (status === 'done') {
      try {
        const responseData = info.file.response;

        if (responseData.message) {
          message.success(`${info.file.name} file uploaded successfully.`);
          showModal(responseData.message); // Покажем модальное окно с сообщением сервера
        } else {
          message.success(`${info.file.name} file uploaded successfully.`);
        }

        if (responseData.data) {
          console.log('Server data:', responseData.data);
        }
      } catch (error) {
        console.error('Error parsing JSON response:', error);
        message.error(`${info.file.name} file uploaded successfully, but failed to parse server response.`);
        showModal("Ошибка разбора ответа сервера.");  // Покажем модальное окно об ошибке
      }
    } else if (status === 'error') {
      message.error(`${info.file.name} file upload failed.`);
      showModal("Ошибка загрузки файла."); // Покажем модальное окно об ошибке
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
                            отправте нам фотографию с потенциальным заболеванием и наш искусственный интелект даст ответ
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
                            <Modal
                            title="Сообщение от сервера"
                            visible={modalVisible}
                            onOk={hideModal}
                            onCancel={hideModal}
                            >
                            <p>{modalContent}</p>
                          </Modal>
                        </div>
                    </div>
                </div>
                <div className="first_background"></div>
            </section>
        </>
    )
}



export default Body;