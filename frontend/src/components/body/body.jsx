import React, { useState } from 'react';
import { Button, Upload, message, Modal } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import '../body/body.css'; // Подключите файл стилей, если он у вас есть

const { Dragger } = Upload;

function Body() {
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

                    if (responseData?.message) {
                        message.success(`${info.file.name} file uploaded successfully.`);
                        showModal(responseData.message);
                    } else {
                        message.success(`${info.file.name} file uploaded successfully.`);
                        showModal(responseData);
                        
                    }

                    if (responseData?.data) {
                        console.log('Server data:', responseData.data);
                    }
                } catch (error) {
                    console.error('Error parsing JSON response:', error);
                    message.error(`${info.file.name} file upload failed to parse server response.`);
                    showModal("Ошибка разбора ответа сервера.");
                }
            } else if (status === 'error') {
                message.error(`${info.file.name} file upload failed.`);
                showModal("Ошибка загрузки файла.");
            }
        },
        onDrop(e) {
            console.log('Dropped files', e.dataTransfer.files);
        },
    };

    return (
        <>
            <section className='first'>
                <div className="first_div">
                    <div className="info_div">
                        <div className="h_div">
                            Проверка онкологии нейросетью
                        </div>
                        <div className="p_div">
                            Отправьте нам фотографию с потенциальным заболеванием, и наш искусственный интеллект даст ответ.
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
                                open={modalVisible}
                                onOk={hideModal}
                                closable={false}
                                footer={[
                                    <Button key="ok" type="primary" onClick={hideModal}>
                                        Ок
                                    </Button>,
                                ]}
                                style={{ top: '30%' }}
                                bodyStyle={{ borderRadius: '0px' }}
                                maskClosable={false}
                                className="custom-modal"
                            >
                                <p>{modalContent}</p>
                            </Modal>
                        </div>
                    </div>
                </div>
                <div className="first_background"></div>
            </section>
        </>
    );
}

export default Body;