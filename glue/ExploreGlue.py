import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame

def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    import pyspark.sql.functions as F
    # convert dymamic frame to data frame
    df = dfc.select(list(dfc.keys())[0]).toDF()
    df = df.withColumn("title", F.upper(F.col("title") ))
    # create dynamic frame from dataframe
    upperDf = DynamicFrame.fromDF(df, glueContext, "filter_votes")
    return(DynamicFrameCollection({"CustomTransform0": upperDf}, glueContext))

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "moviedb", table_name = "ratings", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "moviedb", table_name = "ratings", transformation_ctx = "DataSource0")
## @type: ApplyMapping
## @args: [mappings = [("userid", "long", "userid", "long"), ("movieid", "long", "movieid", "long"), ("rating", "double", "rating", "double"), ("timestamp", "long", "timestamp", "long")], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame = DataSource0]
Transform0 = ApplyMapping.apply(frame = DataSource0, mappings = [("userid", "long", "userid", "long"), ("movieid", "long", "movieid", "long"), ("rating", "double", "rating", "double"), ("timestamp", "long", "timestamp", "long")], transformation_ctx = "Transform0")
## @type: SelectFields
## @args: [paths = ["userid", "movieid", "rating"], transformation_ctx = "Transform6"]
## @return: Transform6
## @inputs: [frame = Transform0]
Transform6 = SelectFields.apply(frame = Transform0, paths = ["userid", "movieid", "rating"], transformation_ctx = "Transform6")
## @type: Filter
## @args: [f = lambda row : (row["rating"] >= 3 and row["rating"] <= 4), transformation_ctx = "Transform3"]
## @return: Transform3
## @inputs: [frame = Transform6]
Transform3 = Filter.apply(frame = Transform6, f = lambda row : (row["rating"] >= 3 and row["rating"] <= 4), transformation_ctx = "Transform3")
## @type: DataSource
## @args: [database = "moviedb", table_name = "movies", transformation_ctx = "DataSource1"]
## @return: DataSource1
## @inputs: []
DataSource1 = glueContext.create_dynamic_frame.from_catalog(database = "moviedb", table_name = "movies", transformation_ctx = "DataSource1")
## @type: ApplyMapping
## @args: [mappings = [("movieid", "long", "movieid", "long"), ("title", "string", "title", "string"), ("genres", "string", "genres", "string")], transformation_ctx = "Transform8"]
## @return: Transform8
## @inputs: [frame = DataSource1]
Transform8 = ApplyMapping.apply(frame = DataSource1, mappings = [("movieid", "long", "movieid", "long"), ("title", "string", "title", "string"), ("genres", "string", "genres", "string")], transformation_ctx = "Transform8")
## @type: DropFields
## @args: [paths = [], transformation_ctx = "Transform2"]
## @return: Transform2
## @inputs: [frame = Transform8]
Transform2 = DropFields.apply(frame = Transform8, paths = [], transformation_ctx = "Transform2")
## @type: CustomCode
## @args: [dynamicFrameConstruction = DynamicFrameCollection({"Transform2": Transform2}, glueContext), className = MyTransform, transformation_ctx = "Transform7"]
## @return: Transform7
## @inputs: [dfc = Transform2]
Transform7 = MyTransform(glueContext, DynamicFrameCollection({"Transform2": Transform2}, glueContext))
## @type: SelectFromCollection
## @args: [key = list(Transform7.keys())[0], transformation_ctx = "Transform1"]
## @return: Transform1
## @inputs: [dfc = Transform7]
Transform1 = SelectFromCollection.apply(dfc = Transform7, key = list(Transform7.keys())[0], transformation_ctx = "Transform1")
## @type: Join
## @args: [keys2 = ["movieid"], keys1 = ["movieid"], transformation_ctx = "Transform4"]
## @return: Transform4
## @inputs: [frame1 = Transform3, frame2 = Transform1]
Transform4 = Join.apply(frame1 = Transform3, frame2 = Transform1, keys2 = ["movieid"], keys1 = ["movieid"], transformation_ctx = "Transform4")
## @type: SelectFields
## @args: [paths = ["userid", "movieid", "rating", "title"], transformation_ctx = "Transform5"]
## @return: Transform5
## @inputs: [frame = Transform4]
Transform5 = SelectFields.apply(frame = Transform4, paths = ["userid", "movieid", "rating", "title"], transformation_ctx = "Transform5")
## @type: DataSink
## @args: [connection_type = "s3", format = "csv", connection_options = {"path": "s3://ctsspark01/movie-ratings-join/", "partitionKeys": []}, transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform5]
DataSink0 = glueContext.write_dynamic_frame.from_options(frame = Transform5, connection_type = "s3", format = "csv", connection_options = {"path": "s3://ctsspark01/movie-ratings-join/", "partitionKeys": []}, transformation_ctx = "DataSink0")
job.commit()