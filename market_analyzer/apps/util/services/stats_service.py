import statistics as stats

class StatsService:

    def getStockAverages(self, results):
        diffs = []
        highestPrices = []
        lowestPrices = []

        for result in results:
            openPrice = result["o"]
            closePrice = result["c"]
            diffs.append(closePrice - openPrice)
            highestPrices.append(result["h"])
            lowestPrices.append(result["l"])

        return {
            "avrgDiff": stats.fmean(diffs), 
            "avrgHighest": stats.fmean(highestPrices),
            "avrgLowest": stats.fmean(lowestPrices),
        }
        