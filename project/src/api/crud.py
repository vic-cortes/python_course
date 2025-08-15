from typing import Any, Dict, Optional, Tuple

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import asc, desc, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ..models.products import Product

"""
Example usage of pagination functions:

1. Basic pagination with default parameters:
    ```python
    products, metadata = get_client_product(db, client_name="home_depot")
    # Returns:
    # - products: Page object with first 10 items
    # - metadata: {
    #     "total_items": 100,
    #     "total_pages": 10,
    #     "current_page": 1,
    #     "page_size": 10,
    #     "has_next": true,
    #     "has_previous": false
    # }
    ```

2. Custom page size and sorting:
    ```python
    products, metadata = get_client_product(
        db,
        client_name="home_depot",
        page=2,
        size=20,
        sort_by="price",
        sort_order="desc"
    )
    # Returns items 21-40 sorted by price in descending order
    ```

3. Using generic paginate_query for custom filters:
    ```python
    filters = {
        "client_name": "home_depot",
        "brand": "Samsung"
    }
    products, metadata = paginate_query(
        db,
        Product,
        page=1,
        size=15,
        filters=filters,
        sort_by="date_created"
    )
    # Returns first 15 Samsung products from home_depot
    ```
"""


def paginate_query(
    db: Session,
    model: Any,
    page: int = 1,
    size: int = 10,
    filters: Optional[Dict[str, Any]] = None,
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
) -> Tuple[Page, Dict[str, Any]]:
    """
    Generic pagination function with support for filtering and sorting.

    Args:
        db: Database session
        model: SQLAlchemy model class
        page: Page number (1-based)
        size: Number of items per page
        filters: Dictionary of field:value pairs for filtering
        sort_by: Field name to sort by
        sort_order: Sort direction ("asc" or "desc")

    Returns:
        Tuple of (Page object with results, metadata dictionary)
    """
    try:
        # Validate page and size
        if page < 1:
            page = 1
        if size < 1:
            size = 10

        # Build base query
        query = select(model)

        # Apply filters
        if filters:
            for field, value in filters.items():
                if hasattr(model, field):
                    query = query.filter(getattr(model, field) == value)

        # Apply sorting
        if sort_by and hasattr(model, sort_by):
            direction = desc if sort_order.lower() == "desc" else asc
            query = query.order_by(direction(getattr(model, sort_by)))

        # Execute paginated query
        params = Params(page=page, size=size)
        paginated_results = paginate(db, query, params)

        # Build metadata
        total = paginated_results.total
        total_pages = (total + size - 1) // size

        metadata = {
            "total_items": total,
            "total_pages": total_pages,
            "current_page": page,
            "page_size": size,
            "has_next": page < total_pages,
            "has_previous": page > 1,
        }

        return paginated_results, metadata

    except SQLAlchemyError as e:
        raise ValueError(f"Database error occurred: {str(e)}")
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")


def get_client_product(
    db: Session,
    client_name: str,
    page: int = 1,
    size: int = 10,
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
) -> Tuple[Page, Dict[str, Any]]:
    """
    Retrieve products for a specific client with pagination support.

    Args:
        db: Database session
        client_name: Name of the client to filter by
        page: Page number (1-based)
        size: Number of items per page
        sort_by: Field to sort results by
        sort_order: Sort direction ("asc" or "desc")

    Returns:
        Tuple of (Page object with results, metadata dictionary)
    """
    filters = {"client_name": client_name}
    return paginate_query(
        db=db,
        model=Product,
        page=page,
        size=size,
        filters=filters,
        sort_by=sort_by,
        sort_order=sort_order,
    )
