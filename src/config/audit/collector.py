class AuditCollector:

    _events = []

    @classmethod
    def add(cls, action: str, entity: str, entity_id=None):
        cls._events.append({
            "action": action,
            "entity": entity,
            "entity_id": entity_id
        })

    @classmethod
    def flush(cls):
        events = cls._events
        cls._events = []
        return events