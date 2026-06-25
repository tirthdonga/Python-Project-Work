import date_time, mathemetic, random_num, file_op, uuid_gene

def module_attributes():
    # Mapping your modules to their objects
    modules = {
        "date_time": date_time,
        "mathemetic": mathemetic,
        "random_num": random_num,
        "file_op": file_op,
        "uuid": uuid_gene
    }
    
    print("\n--- Available Module Attributes ---")
    for name, module in modules.items():
        print(f"\nFunctions in '{name}':")
        for attr in dir(module):
            if not attr.startswith("__"):
                print(f" - {attr}")
                
module_attributes()