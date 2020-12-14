from django.shortcuts import render
import coreapi
from rest_framework.schemas import AutoSchema


class StudentViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('name')
            ]
        manual_fields = super(StudentViewSchema, self).get_manual_fields(path, method)
        return manual_fields + extra_fields
