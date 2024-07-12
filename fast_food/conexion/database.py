#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, logging, csv

from fast_food.define import DATABASE_PATH  

''' Internal Logs '''
def log():
    return logging.getLogger(__name__) #.info() .debug() .warning() .error() 

class DBase:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(f"{DATABASE_PATH}/{name}.db")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            log().warning("Error connecting to the database: %s", e)

    def close(self):
        if self.conn:
            self.conn.commit()
            if self.cursor:
                self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def commit(self):
        self.conn.commit()

    def create(self, columns, table):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table}({columns})"
            self.cursor.execute(query)
            self.commit()
        except sqlite3.Error as e:
            log().warning('Error creating DB table: %s', e)

    def insert(self, table, columns, values):
        try:
            # Asegurarse de que 'values' sea una tupla o lista
            if not isinstance(values, (tuple, list)):
                raise ValueError("Values must be a tuple or a list")

            placeholders = ', '.join(['?'] * len(values))
            query = f'INSERT INTO {table}({columns}) VALUES ({placeholders})'
        
            log().debug("Executing query: %s with values %s", query, values)
        
            self.cursor.execute(query, values)
            self.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            log().warning('Error inserting data into DB: %s', e)
            return None
        except ValueError as ve:
            log().warning('Value error: %s', ve)
            return None

    def update(self, table, set_clause, where_clause):
        try:
            query = f'UPDATE {table} SET {set_clause} WHERE {where_clause}'
            self.cursor.execute(query)
            self.commit()
        except sqlite3.Error as e:
            log().warning('Error updating data in DB: %s', e)

    def delete(self, table, where_clause):
        try:
            query = f'DELETE FROM {table} WHERE {where_clause}'
            self.cursor.execute(query)
            self.commit()
        except sqlite3.Error as e:
            log().warning('Error deleting data from DB: %s', e)

    def findOne(self, table, where_clause):
        aux = []
        try:
            query = f'SELECT * FROM {table} WHERE {where_clause} LIMIT 1'
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            aux.append(result) #if result is not None else None
        except sqlite3.Error as e:
            log().warning('Error finding one record in DB: %s', e)

        return aux if aux is not None else None

    def selectAll(self, table):
        try:
            query = f'SELECT * FROM {table}'
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            log().warning('Error selecting all records from DB: %s', e)
            return None

    @staticmethod
    def to_csv(self, data, fname="output.csv"):
        try:
            with open(fname, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
        except Exception as e:
            log().warning('Error writing to CSV file: %s', e)

