from datetime import datetime

from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from slugify import slugify
from sqlalchemy.ext.asyncio import AsyncSession
from app.backend.db_depends import get_db
from sqlalchemy import select, insert, func, update
from app.schemas import CreateReview
from app.models import *
from app.routers.auth import get_current_user

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.get('/')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    review = await db.scalars(select(Review).where(Review.is_active == True))
    all_reviews = review.all()
    if not all_reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No reviews found")
    return all_reviews


@router.post('/')
async def add_review(db: Annotated[AsyncSession, Depends(get_db)], create_review: CreateReview,
                     get_user: Annotated[dict, Depends(get_current_user)]):
    if not get_user.get('is_customer'):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='This review is only for customer')

    product_id = await db.scalar(
        select(Product.id).where(Product.id == create_review.product_id, Product.is_active == True))
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no product found')

    user_id = get_user.get('id')
    if await db.scalar(
            select(Review.id).where(
                Review.product_id == product_id, Review.user_id == user_id, Review.is_active == True)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User review exists')

    await db.execute(insert(Review).values(
        user_id=user_id,
        product_id=product_id,
        comment=create_review.comment,
        grade=create_review.grade,
    ))
    ev = (
        select(func.avg(Review.grade))
        .where(Review.product_id == product_id, Review.is_active == True)
        .group_by(Review.product_id)
        .scalar_subquery()
    )
    await db.execute(
        update(Product)
        .where(Product.id == product_id)
        .values(rating=ev))
    await db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful',
    }


@router.get('/{product_name}')
async def products_reviews():
    pass


@router.delete('/')
async def delete_reviews():
    pass
