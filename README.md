🦾 Mano Robótica – Proyecto de Control con Sensores Flex, ESP32-S3 y GUI

Este proyecto consiste en el desarrollo de una mano robótica de cinco dedos, controlada mediante un guante instrumentado con sensores flex, un microcontrolador ESP32-S3, y una interfaz gráfica de usuario (GUI) que permite operar el sistema tanto en modo manual como automático.

El proyecto integra mecánica, electrónica, comunicación, e interacción humano–máquina.

Integrantes:
-Cristian Acero
-Camila Cáceres
-Sol Fernández
-Leila Gauna
-Nicolás Silva

📌 Introducción

El proyecto implementa un prototipo funcional de mano robótica controlado desde un guante sensorizado y una interfaz gráfica desarrollada para monitorear y supervisar los movimientos.

La GUI permite:

Inicio de sesión seguro

Control manual mediante sliders

Control automático mediante los sensores flex

Guardar y repetir movimientos

Detener y resetear el sistema

Visualizar estados, eventos y parámetros en tiempo real

El enfoque combina mecánica 3D, electrónica basada en ESP32-S3, sensores resistivos, procesamiento digital, comunicación WiFi y diseño de interfaz gráfica.

🎯 Objetivo General

Desarrollar una interfaz gráfica con autenticación que permita controlar y supervisar la mano robótica manualmente o mediante sensores flex, asegurando seguridad, precisión y usabilidad.

🎯 Objetivos Específicos

Implementar un módulo de login seguro

Incorporar sliders gráficos para cada dedo

Añadir botones para guardar, repetir, detener y resetear movimientos

Integrar un modo automático mediante sensores flex

Establecer comunicación estable con ESP32-S3

Validar la funcionalidad del sistema mediante pruebas con usuarios


🧩 Justificación

El proyecto cubre tres áreas clave:

Mecánica: diseño e impresión 3D de la mano

Electrónica: ADC ADS1115, ESP32-S3, servos MG996R, nivel lógico y alimentación

Interfaz: GUI con autenticación, control manual y automático, visualización y registro de eventos

El alcance es académico y experimental, orientado al estudio de control robótico y sistemas interactivos.

🖥️ Interfaz Gráfica (GUI)

La GUI es el núcleo de interacción con el usuario.

Incluye:

Inicio de sesión

5 sliders para Pulgar, Índice, Medio, Anular y Meñique

Selector de modo Manual/Guante

Estado del sistema

Registro de eventos

Botones de acción: Guardar, Repetir, Resetear, Detener, Volver al login

La interfaz fue desarrollada en Python – Tkinter, con estilo moderno y oscuro.

🧩 Componentes Implementados

Microcontrolador ESP32-S3-WROOM-1-N8

ADC ADS1115 (16 bits, I2C)

5 sensores flex 2.2"

5 servos MG996R

Nivel lógico NBXB0108

Regulador LDO LM1117MPX-3.3

Fuente 5V

Interfaz gráfica en Python

Guante sensorizado

📡 Conexión de Sensores

Cada sensor flex se conecta como divisor de voltaje, y su salida alimenta un canal del ADC ADS1115.

Procesamiento en ESP32:

Filtrado

Calibración (min–max)

Conversión lineal a 0°–180°

Envío de señal PWM al servo correspondiente

🛠️ Conexión con la Base de Datos (Django)

El backend fue implementado en Django y gestiona:

Autenticación

Movimientos guardados

Registro de eventos

Comunicación con la interfaz

Modelos principales:

Usuario

Movimiento

LogEvento

La interfaz se comunica vía HTTP/WebSocket.


