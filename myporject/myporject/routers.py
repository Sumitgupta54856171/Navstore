class MongoDBRouter:
    route_app_labels = {'myapp'}
    mongo_app_labels = {'other_app_for_mongo'}
    mongo_models = {'ImageMongo'}  

    def db_for_read(self, model, **hints):
        """Route read operations based on app label or model name."""
        if model._meta.app_label in self.route_app_labels:
           
            if model.__name__ in self.mongo_models:
                return 'mongodb'
            return 'default'  # PostgreSQL
        
        if model._meta.app_label in self.mongo_app_labels:
            return 'mongodb'
        
        return None

    def db_for_write(self, model, **hints):
        """Route write operations based on app label or model name."""
        if model._meta.app_label in self.route_app_labels:
            if model.__name__ in self.mongo_models:
                return 'mongodb'
            return 'default'  # PostgreSQL
        
        if model._meta.app_label in self.mongo_app_labels:
            return 'mongodb'
        
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations within the same database."""
        db_set = {'default', 'mongodb'}
        
        # Get the databases for both objects
        obj1_db = self.db_for_read(obj1.__class__)
        obj2_db = self.db_for_read(obj2.__class__)
        
        # Allow relations if both objects use the same database
        if obj1_db and obj2_db:
            return obj1_db == obj2_db
        
        # Allow relations within PostgreSQL (default behavior)
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
            
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Control which migrations run on which database."""
        if app_label in self.route_app_labels:
            # Check if it's a MongoDB model
            if model_name and model_name in [m.lower() for m in self.mongo_models]:
                return db == 'mongodb'
            return db == 'default'  # PostgreSQL
        
        if app_label in self.mongo_app_labels:
            return db == 'mongodb'
        
        return None