import os
from datetime import datetime
import cv2
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table


def add_to_origin_table(file_name):
    add_to_any_table(file_name, "Original")


def add_to_edited_table(file_name):
    add_to_any_table(file_name, "Edited")









