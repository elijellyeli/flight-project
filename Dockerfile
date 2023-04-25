FROM mageai/mageai:latest

ARG PROJECT_NAME=flight
ARG MAGE_CODE_PATH=/home/mage_code
ARG USER_CODE_PATH=${MAGE_CODE_PATH}/${PROJECT_NAME}


# COPY ${PROJECT_NAME} ${PROJECT_NAME}

WORKDIR ${USER_CODE_PATH}

# Set the USER_CODE_PATH variable to the path of user project.
ENV USER_CODE_PATH=${USER_CODE_PATH}

# Copy Requirements
# COPY requirements.txt ${USER_CODE_PATH}/requirements.txt
# Install custom Python libraries
# RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
# Install custom libraries within 3rd party libraries (e.g. DBT packages)
# RUN python3 /app/install_other_dependencies.py --path ${USER_CODE_PATH}

ENV PYTHONPATH="${PYTHONPATH}:${MAGE_CODE_PATH}"
ENV BLAT="BLAT"

CMD ["/bin/sh", "-c", "/app/run_app.sh"]