class LegacyRouter:
    """
    Um roteador de banco de dados para direcionar operações de banco de dados para o banco de dados 'dashboards_old' para
    os modelos do aplicativo 'legacy'.
    """
    def db_for_read(self, model, **hints):
        """
        Direcione operações de leitura para 'dashboards_old' se o modelo for do app 'legacy'.
        """
        if model._meta.app_label == 'legacy':
            return 'dashboards_old'
        return None

    def db_for_write(self, model, **hints):
        """
        Direcione operações de escrita para 'dashboards_old' se o modelo for do app 'legacy'.
        """
        if model._meta.app_label == 'legacy':
            return 'dashboards_old'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permita relações se um modelo em 'legacy' estiver envolvido.
        """
        if obj1._meta.app_label == 'legacy' or obj2._meta.app_label == 'legacy':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Evite migrações para o banco de dados 'dashboards_old'.
        """
        if app_label == 'legacy':
            return db == 'dashboards_old'
        return None
