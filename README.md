# Navier Stokes Experiments

Este repositorio contiene experimentos sobre Navier Stokes
para la materia Computación Paralela 2021 de FaMAF, UNC, Córdoba.

## Requerimientos

Para poder reproducir los experimentos es necesario:

- Una distribución Debian o Ubuntu.
- Ansible
    ```
    sudo apt install ansible
    ```
- Correr el ansible playbook
    ```
    sudo ansible-playbook dependencias.yml
    ```
- Python3 y un entorno virtual
    Si ya sos desarrolladore python tendrás tu forma de creartelo, si no,
    esta es una forma posible:
    - Instalar pyenv y pyenv-virtualenv
        ```
        curl https://pyenv.run | bash
        exec $SHELL
        git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
        ```
    - Verificar la versión actual de python con
        ```
        pyenv version
        ```
    - Si no es una versión de python 3, instalar python 3.9.4
        ```
        pyenv install 3.9.4
        pyenv global 3.9.4
        ```
    - Crear un entorno virtual
        ```
        pyenv virtualenv navier-stokes
        ```
- Instalar dependencias de python
    - Activar entorno virtual
        ```
        pyenv activate navier-stokes
        ```
    - Instalar
        ```
        pip install -r requirements.txt
        ```
