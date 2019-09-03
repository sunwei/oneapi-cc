# coding: utf-8
from oneapi.utils import (get_dict_from_base64_data)

BASE64_JSON_FILE = 'ewogICJ2ZXJzaW9uIjogInYxIiwKICAibmFtZXNwYWNlIjogIndhcmVob3VzZSIs' \
                   'CiAgIm1ldGFkYXRhIjogewogICAgImF1dGhvciI6ICJTdW4gV2VpIiwKICAgICJl' \
                   'bWFpbCI6ICJ3YXlkZS5zdW5AZ21haWwuY29tIiwKICAgICJyZXBvc2l0b3J5Ijog' \
                   'Imh0dHBzOi8vZ2l0aHViLmNvbS9zdW53ZWkvZmxhc2stc2FtbDItb2t0YSIsCiAg' \
                   'ICAiZGVzY3JpcHRpb24iOiAidXNlZCBmb3Igd2hhdC4uLiIKICB9LAogICJhcGlz' \
                   'IjogWwogICAgewogICAgICAibmFtZSI6ICJXYXJlaG91c2UgSW52ZW50b3J5IiwK' \
                   'ICAgICAgInNwZWNzIjogImh0dHBzOi8vZXhhbXBsZS5jb20vc3dhZ2dlci5qc29u' \
                   'IiwKICAgICAgInBhdGgiOiAiL3dhcmVob3VzZS9pbnZlbnRvcnkiLAogICAgICAi' \
                   'ZGVzY3JpcHRpb24iOiAidXNlZCBmb3Igd2hhdC4uLiIsCiAgICAgICJhbm5vdGF0' \
                   'aW9ucyI6ICJsYWJlbHMgb3IgdGFncy4uLiIKICAgIH0sCiAgICB7CiAgICAgICJu' \
                   'YW1lIjogIldhcmVob3VzZSBQcmljaW5nIiwKICAgICAgInNwZWNzIjogImh0dHBz' \
                   'Oi8vZXhhbXBsZS5jb20vc3dhZ2dlci5qc29uIiwKICAgICAgInBhdGgiOiAiL3dh' \
                   'cmVob3VzZS9wcmljaW5nIiwKICAgICAgImRlc2NyaXB0aW9uIjogInVzZWQgZm9y' \
                   'IHdoYXQuLi4iLAogICAgICAiYW5ub3RhdGlvbnMiOiAibGFiZWxzIG9yIHRhZ3Mu' \
                   'Li4iCiAgICB9CiAgXSwKICAidXBzdHJlYW1zIjogWwogICAgewogICAgICAibmFt' \
                   'ZSI6ICJJbnZlbnRvcnkiLAogICAgICAiZW5kcG9pbnRzIjogWwogICAgICAgICJh' \
                   'cGkxLmNvbSIsCiAgICAgICAgImFwaTIuY29tIiwKICAgICAgICAiYXBpMy5jb20i' \
                   'CiAgICAgIF0KICAgIH0sCiAgICB7CiAgICAgICJuYW1lIjogIlByaWNpbmciLAog' \
                   'ICAgICAiZW5kcG9pbnRzIjogWwogICAgICAgICJhcGkzLmNvbSIsCiAgICAgICAg' \
                   'ImFwaTQuY29tIiwKICAgICAgICAiYXBpNS5jb20iCiAgICAgIF0KICAgIH0KICBd' \
                   'LAogICJyb3V0ZVNwZWNpZmljYXRpb25zIjogWwogICAgewogICAgICAiYXBpUmVm' \
                   'IjogIldhcmVob3VzZSBJbnZlbnRvcnkiLAogICAgICAidXBzdHJlYW1SZWYiOiAi' \
                   'SW52ZW50b3J5IiwKICAgICAgInBvbGljaWVzIjp7CiAgICAgICAgImF1dGhlbnRp' \
                   'Y2F0aW9uIjogewogICAgICAgICAgInR5cGUiOiAiQmFzaWMiCiAgICAgICAgfQog' \
                   'ICAgICB9CiAgICB9LCB7CiAgICAgICJhcGlSZWYiOiAiV2FyZWhvdXNlIFByaWNp' \
                   'bmciLAogICAgICAidXBzdHJlYW1SZWYiOiAiUHJpY2luZyIsCiAgICAgICJwb2xp' \
                   'Y2llcyI6ewogICAgICAgICJhdXRoZW50aWNhdGlvbiI6IHsKICAgICAgICAgICJ0' \
                   'eXBlIjogIkJhc2ljIgogICAgICAgIH0KICAgICAgfQogICAgfQogIF0KfQ=='

BASE64_YAML_FILE = 'b25lYXBpOiAiMS4wLjAiCm5hbWVzcGFjZTogZGVmYXVsdAptZXRhZGF0YToKICBh' \
                   'dXRob3I6IHdheWRlLnN1bkBnbWFpbC5jb20KICBnaXRodWI6IGh0dHBzOi8vZ2l0' \
                   'aHViLmNvbS9zdW53ZWkvZmxhc2stc2FtbDItb2t0YQogIG5hbWU6IFNpbXBsZSBB' \
                   'UEkgb3ZlcnZpZXcKICBkZXNjcmlwdGlvbjogdXNlZCBmb3Igd2hhdC4uLgogIGFu' \
                   'bm90YXRpb25zOgogICAgZGVzY3JpcHRpb25zIGFuZCB0YWdzCmFwaXM6CiAgLSAv' \
                   'd2FyZWhvdXNlL2ludmVudG9yeToKICAgICAgZW5kcG9pbnRzOgogICAgICAgIC0g' \
                   'YXBpMS5jb20KICAgICAgICAtIGFwaTIuY29tCiAgICAgICAgLSBhcGkzLmNvbQog' \
                   'IC0gL3dhcmVob3VzZS9wcmljaW5nOgogICAgICBlbmRwb2ludHM6CiAgICAgICAg' \
                   'LSBhcGk0LmNvbQogICAgICAgIC0gYXBpNS5jb20KICAgICAgICAtIGFwaTYuY29t'

NOT_FILE = 'bm90Cg=='


def test_get_file_format():
    assert get_dict_from_base64_data(BASE64_YAML_FILE) is not None
    assert get_dict_from_base64_data(BASE64_JSON_FILE) is not None
    assert get_dict_from_base64_data(NOT_FILE) is None

