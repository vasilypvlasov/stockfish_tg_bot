def error(update, context):
    """Log Errors"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
