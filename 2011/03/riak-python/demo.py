### @export "imports"
import csv
import json
import riak

### @export "load-data"
client = riak.RiakClient()
bucket = client.bucket('goog')

f = open("dexy--goog.csv", "r")
for row in csv.DictReader(f):
    key = row['Date'] # Dates are unique, use as keys.
    if not bucket.get(key).exists():
        item = bucket.new(key, data=row)
        item.store()

f.close()

### @export "show-record"
bucket.get("2010-05-05").get_data()

### @export "simple-map"
query = client.add('goog')
query.map("Riak.mapValuesJson")
results = query.run()

### @export "simple-map-len-results"
len(results)


### @export "simple-map-first-record"
results[0]
results[0]['Date']
results[0]['Volume']

### @export "simple-map-specific-dates"
query = client.add("goog","2010-01-04")
query.add("goog","2010-01-05")
query.add("goog","2010-01-06")
query.add("goog","2010-01-07")
query.add("goog","2010-01-08")
query.map("Riak.mapValuesJson")
results = query.run()
for r in results:
    print r

### @export "simple-map-reduce"
query = client.add("goog","2010-01-04")
query.add("goog","2010-01-05")
query.add("goog","2010-01-06")
query.add("goog","2010-01-07")
query.add("goog","2010-01-08")
query.map("""function(value) {
    var data = Riak.mapValuesJson(value)[0];
    return [data.High];
}""")
query.reduce("Riak.reduceMax")
first_week_jan_max = query.run()[0]
first_week_jan_max

### @export "map-highs-by-month"
query = client.add('goog')
query.map("""function(value, keyData, arg) {
    var data = Riak.mapValuesJson(value)[0];
    var month = value.key.split('-').slice(0,2).join('-');
    var obj = {};
    obj[month] = data.High;
    return [obj];
}""")
query.reduce("""function(values, arg) {
    return [ values.reduce(function(acc, item) {
    for(var month in item) {
        if(acc[month]) {
            acc[month] = (acc[month] < item[month]) ?  item[month] : acc[month];
        } else {
            acc[month] = item[month];
        }
    }
return acc; })];
}""")

monthly_highs = query.run()
for k in sorted(monthly_highs[0].keys())[0:5]:
    print "high in month", k, "was", monthly_highs[0][k]


### @export "find-days-over-600"
js = """function(value, keyData, arg) {
  var data = Riak.mapValuesJson(value)[0];
  if(data.High && data.High > 600.00)
    return [value.key];
  else
    return [];
}"""

query = client.add('goog')
query.map(js)
days_over_600 = query.run()
len(days_over_600)

### @export "save-data"
f = open("dexy--highs-by-month.csv", "w")
w = csv.writer(f)
for k, v in monthly_highs[0].items():
    w.writerow([k, v])

f.close()


data = {
    "number-days-over-600" : len(days_over_600),
    "first-week-jan-max" : first_week_jan_max
}

f = open("dexy--map-reduce-results.json", "w")
json.dump(data,f)
f.close()

