from flask import request
from RestplusAPI.api.myapi import api
from flask_restplus import Resource
from RestplusAPI.api.shop.api_definition import page_with_products, product
from RestplusAPI.api.shop.parsers import pagination_parser as pagination


namespace = api.namespace('shop/products', description='Ops on my shop items')


@namespace.route('/')
class Offer(Resource):

    @api.expect(pagination)
    @api.marschal_with(page_with_products)
    def get(self):
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        items_per_page = args.get('items_per_page', 10)
        return products

    @api.expect(product)
    def post(self):
        return None, 200
