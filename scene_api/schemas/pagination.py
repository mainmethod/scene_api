from marshmallow import fields, post_load, Schema

MAX_PER_PAGE = 25


class PaginationSchema(Schema):
    """Basic Schema for limit/offset pagination"""

    page = fields.Int(missing=1)
    per_page = fields.Int(missing=MAX_PER_PAGE)

    @post_load
    def ensure_max_per_page(self, data, **kwargs):
        """ensure per_page is not greater than max_per_page"""
        if data.get("per_page") > MAX_PER_PAGE:
            data["per_page"] = MAX_PER_PAGE
        return data


pagination_schema = PaginationSchema()
