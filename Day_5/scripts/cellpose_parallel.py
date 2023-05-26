#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Copyright (c) 2023 University of Dundee.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions
#   are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#   ARE DISCLAIMED.
#   IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY
#   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#   HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#   LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
#   OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
#   DAMAGE.
#
# Version: 1.0
#

import dask
import dask.array as da

import time

from cellpose import io, models, utils

# Dask array loaded from S3
data = None
ENDPOINT_URL = 'https://uk1s3.embassy.ebi.ac.uk/'


# Load-binary
def load_binary_from_s3(name, resolution='0'):
    root = '%s/%s/' % (name, resolution)
    return da.from_zarr(ENDPOINT_URL + root)


# Analyse the image using cellpose
def analyze(z):
    t = 0
    channels = [[0, 1]]
    model = models.Cellpose(gpu=False, model_type='cyto')
    cellpose_masks, flows, styles, diams = model.eval(data[t, :, z, :, :], diameter=None, channels=channels)  # noqa
    return cellpose_masks, z


# Build task graph
def build_task_graph(range_z):
    lazy_results = []
    middle_z = data.shape[2] // 2
    for z in range(middle_z - range_z, middle_z + range_z):
        lazy_result = dask.delayed(analyze)(z)
        lazy_results.append(lazy_result)
    return lazy_results


# Compute
def compute(lazy_results):
    return dask.compute(*lazy_results)


# Save results
def save_results_locally(results, name):
    for i in range(len(results)):
        r, z = results[i]
        n = name.replace("/", "_") + "_" + str(z)
        outlines = utils.outlines_list(r)
        io.outlines_to_text(n, outlines)
     
# main
def main():
    # Collect image ID
    image_id = "6001247"
    range_z = 2  # Set to 1 when running against the BIA image (demo)

    # Retrieve the cellpose model
    models.Cellpose(gpu=False, model_type='cyto')
    global data
    name = 'idr/zarr/v0.1/%s.zarr' % (image_id)
    # name = 'bia-integrator-data/S-BIAD338/804b2976-1111-4099-8bfc-21d1d1d2163c/804b2976-1111-4099-8bfc-21d1d1d2163c.zarr/0'  # noqa

    data = load_binary_from_s3(name)
    print("Dask array: %s" % data)

    lazy_results = build_task_graph(range_z)

    start = time.time()
    results = compute(lazy_results)
    elapsed = time.time() - start
    print('Compute time (in seconds): %s' % elapsed)
    save_results_locally(results, name)
    print('done')


if __name__ == "__main__":
    main()
