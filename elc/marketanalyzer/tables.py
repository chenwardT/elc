
# Table to display market records of (potentially multiple) types.
class RecordTable(tables.Table):
    # since MarketRecord doesn't directly hold typeName, we must override the
    #  accessor to follow the FK to get it
    type_name = tables.Column(accessor='typeID.typeName')
    regionName = tables.Column(accessor='stationID.regionID.regionName')
    security = tables.Column(accessor='stationID.solarSystemID.security')
    stationName = tables.Column(accessor='stationID.stationName')
    
    # TO DO: -remove fields from models so we don't have to hide so much
    #        -hide itemName col from detail views
    #        -get price to align right and force 2 decimal places shown
    id = tables.Column(visible=False)
    typeID = tables.Column(visible=False)
    range = tables.Column(visible=False)
    orderID = tables.Column(visible=False)
    jumps = tables.Column(visible=False)
    bid = tables.Column(visible=False)
    minVolume = tables.Column(visible=False)
    solarSystemName = tables.Column(visible=False)
    stationID = tables.Column(visible=False)
    
    def render_price(self, value):
        return '%s' % locale.format('%.2f', value, grouping=True)
        
    def render_security(self, value):
        return '%.1f' % value
    
    # django-tables2 offers automatic generation of columns based on a model
    # NOTE: Col sorting is handled by the DB when table is backed by a model
    class Meta:
        model = MarketRecord
        attrs = {'class': 'paleblue'}
        sequence = ('security', 'regionName', 'stationName',
                    'type_name', 'price', 'volEntered', 'volRemaining', '...')

# Table of order info used by the type_detail view.
class DetailTable(RecordTable):
    regionName = tables.Column(accessor='stationID.regionID.regionName',
                               verbose_name='Region')
    solarSystemName = tables.Column(accessor='stationID.solarSystemID.solarSystemName',
                                    verbose_name='Solar System')
    security = tables.Column(accessor='stationID.solarSystemID.security')
    stationName = tables.Column(accessor='stationID.stationName',
                                verbose_name='Station')
    id = tables.Column(visible=False)
    typeID = tables.Column(visible=False)
    range = tables.Column(visible=False)
    orderID = tables.Column(visible=False)
    jumps = tables.Column(visible=False)
    bid = tables.Column(visible=False)
    type_name = tables.Column(visible=False)
    minVolume = tables.Column(visible=False)
    solarSystemName = tables.Column(visible=False)
    stationID = tables.Column(visible=False)
    volEntered = tables.Column(visible=False)
    volRemaining = tables.Column(verbose_name='Qty')
    
    class Meta:
        model = MarketRecord
        attrs = {'class': 'paleblue'}
        sequence = ('security', 'regionName', 'stationName',
                    'price', 'volRemaining', '...')
        exclude = {'id', 'typeID', 'range', 'orderID', 'jumps', 'bid', }

# Table to display results of an LP search.
class LPResults(tables.Table):
    corp = tables.Column(verbose_name='Corporation')
    itemName = tables.Column(verbose_name='Item')
    qty = tables.Column(verbose_name='Qty')
    ISKcost = tables.Column(verbose_name='ISK Cost')
    LPcost = tables.Column(verbose_name='LP Cost')
    
    class Meta:
        attrs = {'class': 'paleblue'}

# Table to display results of LP calculator. Shown in step 2.
class LPCalcResultsTable(tables.Table):
    itemName = tables.Column(verbose_name='Item')
    regionName = tables.Column(verbose_name='Region')
    sellPrice = tables.Column(verbose_name='Sell Price')
    storeFee = tables.Column(verbose_name='Store Fee')
    otherFee = tables.Column(verbose_name='Other Fee')
    lpCost = tables.Column(verbose_name='LP Cost')
    profitPer = tables.Column()
    profit = tables.Column()
    
    def render_sellPrice(self, value):
        return '%s' % locale.format('%.2f', value, grouping=True)
    
    def render_storeFee(self, value):
        return '%s' % locale.format('%.2f', value, grouping=True)
        
    def render_otherFee(self, value):
        return '%s' % locale.format('%.2f', value, grouping=True)
    
    def render_profitPer(self, value):
        return '%s' % locale.format('%.2f', value, grouping=True)
    
    def render_profit(self, value):
        return '%s' % locale.format('%.2f', value, grouping=True)
    
    class Meta:
        attrs = {'class': 'paleblue'}