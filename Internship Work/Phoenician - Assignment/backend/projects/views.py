# import json
# import os
# import uuid
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.conf import settings

# class ItemDetailView(APIView):
#     def get(self, request):
#         item_code = request.query_params.get('item_code', '')
#         file_path = os.path.join(settings.BASE_DIR, 'projects', 'data', 'data.json')
        
#         # Load JSON data
#         with open(file_path, 'r') as file:
#             data = json.load(file)

#         # Track the last non-null ITEM to use as prefix for null ITEM values
#         last_prefix = ""

#         for item in data:
#             # Check if ITEM is non-null and update last_prefix
#             if item.get('ITEM'):
#                 last_prefix = item['ITEM']
#             else:
#                 # For items with null or empty ITEM, assign a unique ID prefixed with the last non-null ITEM
#                 item['ITEM'] = f"{last_prefix}.{str(uuid.uuid4())[:8]}"  # Unique ID with last prefix

#         if item_code:
#             # Filter for items that are direct children of the provided item_code
#             level = item_code.count('.') + 1
#             data = [item for item in data if item.get('ITEM', '').startswith(f"{item_code}.") and item['ITEM'].count('.') == level]

#         return Response(data)


import json
import os
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class ItemDetailView(APIView):
    def get(self, request):
        item_code = request.query_params.get('item_code', '')
        file_path = os.path.join(settings.BASE_DIR, 'projects', 'data', 'data.json')
        
        # Load JSON data
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Track the last non-null ITEM to use as a prefix for null ITEM values
        last_prefix = ""

        # Modify items in-place to maintain the original order
        for item in data:
            # Update the last_prefix if ITEM is non-null
            if item.get('ITEM'):
                last_prefix = item['ITEM']
            else:
                # Assign a unique ID prefixed with the last non-null ITEM for null ITEM values
                item['ITEM'] = f"{last_prefix}.{str(uuid.uuid4())[:8]}"  # Unique ID with last prefix

        # Filter for direct children if item_code is provided
        if item_code:
            level = item_code.count('.') + 1
            data = [item for item in data if item.get('ITEM', '').startswith(f"{item_code}.") and item['ITEM'].count('.') == level]

        return Response(data)
