import os
from datetime import datetime
import cv2
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table


def add_to_origin_table(file_name):
    add_to_any_table(file_name, "Original")


def add_to_edited_table(file_name):
    add_to_any_table(file_name, "Edited")

def add_to_any_table(file_name, table_name):
    try:
        engine = create_engine('sqlite:///Save_image.db', echo=False)
        conn = engine.connect()
        meta = MetaData(engine)
        table = Table(
            table_name, meta,
            Column('id', Integer, primary_key=True),
            Column('filename', String, nullable=False),
            Column('date_time', String, nullable=False),
        )
        meta.create_all(engine)
        s = table.select()
        result = conn.execute(s)
        extension = file_name.find('.')
        counter = 0
        for i in result:
            if i[1] == file_name or i[1] == file_name[:extension] + str(counter) + file_name[extension:]:
                counter = counter + 1
        if counter > 0:
            file_name = file_name[:extension] + str(counter) + file_name[extension:]
        current_datetime = datetime.now()
        conn.execute(table.insert(), [
            {'filename': file_name, 'date_time': str(current_datetime)}])
    except Exception as e:
        print("Error!", e.__class__, "occurred.")


def save_original_image(image, image_name):
    counter = save_any_image(image, image_name, "Original", 1)
    print(counter)
    return counter

def save_edited_image(image, image_name):
    save_any_image(image, image_name, "Edited", 2)


def save_any_image(image, file_name, path, num):
    try:
        if os.path.exists(path) == 0:
            os.mkdir(path)
            os.chmod(path, 0o777)
        directory = os.path.join(os.path.abspath(os.curdir), path)
        list_of_files = os.listdir(directory)
        extension = file_name.find('.')
        counter = 0
        for i in list_of_files:
            if i == file_name or i == file_name[:extension] + str(counter) + file_name[extension:]:
                counter = counter + 1
        if counter >= 0:
            file_name = file_name[:extension] + str(counter) + file_name[extension:]
        path = os.path.join(directory, file_name)
        if num == 1:
            cv2.imwrite(path, image)
        else:
            image.save(path)
    except Exception as e:
        print("Error!", e.__class__, "occurred.")
    return counter








