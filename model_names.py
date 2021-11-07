# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:39:02 2021

@author: sidkadam
"""

from pydantic import BaseModel

class model_names(BaseModel):
    Number_of_Man:int
    Number_of_Women:int
    Age_between_15_to_25:int 
    Age_between_25_to_45:int
    Dutch_achtergond:int
    Western_migration_background:int 
    Single:int 
    Total: int
    Born_between_1975_to_1985:int
    Meergezins:int
    Persons_with_unemployment_benefits:int
    address:int 