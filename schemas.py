"""
Database Schemas for Calorie Vision App

Each Pydantic model represents a collection in MongoDB.
Collection name is the lowercase of the class name.

- User -> "user"
- Meal -> "meal"
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict

class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Unique email address")
    password_hash: str = Field(..., description="BCrypt password hash")
    is_active: bool = Field(True, description="Whether user is active")

class Macro(BaseModel):
    carbs_g: Optional[float] = Field(None, ge=0)
    protein_g: Optional[float] = Field(None, ge=0)
    fat_g: Optional[float] = Field(None, ge=0)

class Meal(BaseModel):
    user_id: Optional[str] = Field(None, description="User ObjectId as string")
    image_name: Optional[str] = Field(None, description="Uploaded image file name")
    dish_name: Optional[str] = Field(None, description="Detected dish name")
    calories: Optional[float] = Field(None, ge=0, description="Estimated calories (kcal)")
    macros: Optional[Macro] = None
    ingredients: Optional[List[str]] = None
    notes: Optional[str] = None
    source: Optional[str] = Field("openai-vision", description="Analyzer model/provider used")
    raw_response: Optional[Dict] = None
