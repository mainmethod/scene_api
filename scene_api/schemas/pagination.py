from marshmallow import fields, post_load, pre_dump, Schema

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


class PaginationResponseSchema(Schema):
    """Schema list pagination endpoints"""

    total = fields.Int(dump_only=True)
    pages = fields.Int(dump_only=True)
    next = fields.Method("get_next")
    prev = fields.Method("get_prev")

    def get_next(self, obj):
        if obj["has_next"] is True:
            next_num = obj["next_num"]
            path = self.context.get("path", "")
            return f"/api/{path}?page={next_num}"

    def get_prev(self, obj):
        if obj["has_prev"] is True:
            prev_num = obj["prev_num"]
            path = self.context.get("path", "")
            return f"/api/{path}?page={prev_num}"

    @pre_dump
    def to_dict(self, data, **kwargs):
        return {
            "total": data.total,
            "pages": data.pages,
            "next_num": data.next_num,
            "prev_num": data.prev_num,
            "has_next": data.has_next,
            "has_prev": data.has_prev,
        }
