from django.apps import apps


def get_all(folder_name: str, model_name: str):
    product_model = apps.get_model(folder_name, model_name)
    products = product_model.objects.filter(status=True)

    return products


def get_all_by_category(folder_name: str, model_name: str, category: str):
    product_model = apps.get_model(folder_name, model_name)
    products = product_model.objects.filter(tags__title=category, status=True)

    return products
