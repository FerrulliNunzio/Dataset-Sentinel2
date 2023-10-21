class ExportOption:

    __ExportOption: dict = None

    """
        Nome: __init__
        
        Input: image, description, folder, file_name_prefix, region, file_format, crs, crs_transfrorm
        
        Output: //
        
        Comportamento: Inizializza la variabile __ExportOption
    """
    def __init__(self, image, description, folder, file_name_prefix, region, file_format, crs, crs_transfrorm):
        self.__ExportOptions = {
            'image': image,
            'description': description,
            'folder': folder,
            'fileNamePrefix': file_name_prefix,
            'region': region,
            'fileFormat': file_format,
            'maxPixels': 10000000000000,
            'crs': crs,
            'crsTransform': crs_transfrorm,
            'formatOptions': {
                'cloudOptimized': True
            }
        }

    """
        Nome: get_export_option

        Input: //

        Output: dict

        Comportamento: restituisce la variabile __ExportOption
    """
    def get_export_option(self):
        return self.__ExportOptions